// Main JavaScript functionality for Flask Auth App

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert-dismissible');
        alerts.forEach(function(alert) {
            if (alert) {
                var bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        });
    }, 5000);

    // Form validation enhancement
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Password strength checker
    var passwordField = document.getElementById('password');
    if (passwordField) {
        passwordField.addEventListener('input', function() {
            checkPasswordStrength(this.value);
        });
    }

    // Confirm password matching
    var confirmPasswordField = document.getElementById('passwordConfirm');
    if (confirmPasswordField && passwordField) {
        confirmPasswordField.addEventListener('input', function() {
            checkPasswordMatch(passwordField.value, this.value);
        });
    }

    // Loading states for forms
    var submitButtons = document.querySelectorAll('form button[type="submit"]');
    submitButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var form = this.closest('form');
            if (form.checkValidity()) {
                showLoadingState(this);
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Theme toggle functionality
    var themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            toggleTheme();
        });
        
        // Load saved theme
        loadTheme();
    }
});

// Password strength checker function
function checkPasswordStrength(password) {
    var strength = 0;
    var strengthIndicator = document.getElementById('password-strength');
    var strengthText = document.getElementById('password-strength-text');
    
    if (!strengthIndicator) return;
    
    // Length check
    if (password.length >= 8) strength += 1;
    if (password.length >= 12) strength += 1;
    
    // Character variety checks
    if (/[a-z]/.test(password)) strength += 1;
    if (/[A-Z]/.test(password)) strength += 1;
    if (/[0-9]/.test(password)) strength += 1;
    if (/[^A-Za-z0-9]/.test(password)) strength += 1;
    
    // Update strength indicator
    strengthIndicator.className = 'password-strength';
    if (strength < 3) {
        strengthIndicator.classList.add('weak');
        if (strengthText) strengthText.textContent = 'Weak';
    } else if (strength < 5) {
        strengthIndicator.classList.add('medium');
        if (strengthText) strengthText.textContent = 'Medium';
    } else {
        strengthIndicator.classList.add('strong');
        if (strengthText) strengthText.textContent = 'Strong';
    }
}

// Password match checker
function checkPasswordMatch(password, confirmPassword) {
    var confirmField = document.getElementById('passwordConfirm');
    var matchIndicator = document.getElementById('password-match');
    
    if (!confirmField) return;
    
    if (password === confirmPassword && password.length > 0) {
        confirmField.classList.remove('is-invalid');
        confirmField.classList.add('is-valid');
        if (matchIndicator) {
            matchIndicator.textContent = 'Passwords match';
            matchIndicator.className = 'text-success small';
        }
    } else if (confirmPassword.length > 0) {
        confirmField.classList.remove('is-valid');
        confirmField.classList.add('is-invalid');
        if (matchIndicator) {
            matchIndicator.textContent = 'Passwords do not match';
            matchIndicator.className = 'text-danger small';
        }
    } else {
        confirmField.classList.remove('is-valid', 'is-invalid');
        if (matchIndicator) {
            matchIndicator.textContent = '';
        }
    }
}

// Show loading state for buttons
function showLoadingState(button) {
    var originalText = button.innerHTML;
    var loadingText = button.getAttribute('data-loading-text') || 'Loading...';
    
    button.innerHTML = '<span class="loading-spinner me-2"></span>' + loadingText;
    button.disabled = true;
    
    // Reset after 10 seconds (failsafe)
    setTimeout(function() {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 10000);
}

// Theme toggle functionality
function toggleTheme() {
    var currentTheme = document.documentElement.getAttribute('data-theme');
    var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Update theme toggle button
    var themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        var icon = themeToggle.querySelector('i');
        if (icon) {
            if (newTheme === 'dark') {
                icon.className = 'fas fa-sun';
            } else {
                icon.className = 'fas fa-moon';
            }
        }
    }
}

// Load saved theme
function loadTheme() {
    var savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    var themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        var icon = themeToggle.querySelector('i');
        if (icon) {
            if (savedTheme === 'dark') {
                icon.className = 'fas fa-sun';
            } else {
                icon.className = 'fas fa-moon';
            }
        }
    }
}

// Utility functions
function showNotification(message, type = 'info') {
    var notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '9999';
    notification.style.minWidth = '300px';
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(function() {
        if (notification.parentNode) {
            var bsAlert = new bootstrap.Alert(notification);
            bsAlert.close();
        }
    }, 5000);
}

// Copy to clipboard function
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showNotification('Copied to clipboard!', 'success');
    }).catch(function() {
        // Fallback for older browsers
        var textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showNotification('Copied to clipboard!', 'success');
    });
}

// Form data serializer
function serializeForm(form) {
    var formData = new FormData(form);
    var data = {};
    
    for (var pair of formData.entries()) {
        data[pair[0]] = pair[1];
    }
    
    return data;
}

// AJAX form submission helper
function submitFormAjax(form, successCallback, errorCallback) {
    var formData = new FormData(form);
    var submitButton = form.querySelector('button[type="submit"]');
    
    if (submitButton) {
        showLoadingState(submitButton);
    }
    
    fetch(form.action, {
        method: form.method || 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (successCallback) successCallback(data);
        } else {
            if (errorCallback) errorCallback(data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        if (errorCallback) errorCallback({error: 'Network error occurred'});
    })
    .finally(() => {
        if (submitButton) {
            submitButton.innerHTML = submitButton.getAttribute('data-original-text') || 'Submit';
            submitButton.disabled = false;
        }
    });
}

// Input validation helpers
function validateEmail(email) {
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePassword(password) {
    // At least 8 characters, 1 uppercase, 1 lowercase, 1 number
    var re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$/;
    return re.test(password);
}

// Debounce function for search inputs
function debounce(func, wait, immediate) {
    var timeout;
    return function executedFunction() {
        var context = this;
        var args = arguments;
        var later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}