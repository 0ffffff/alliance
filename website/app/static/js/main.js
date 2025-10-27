// Page Navigation
function showPage(pageId) {
  // Hide all pages
  const pages = document.querySelectorAll('.page');
  pages.forEach(page => page.classList.remove('active'));
  
  // Show selected page
  const targetPage = document.getElementById(pageId);
  if (targetPage) {
    targetPage.classList.add('active');
  }
  
  // Scroll to top
  window.scrollTo(0, 0);
}

// Smooth scroll to features section
function scrollToFeatures() {
  const featuresSection = document.getElementById('features-section');
  if (featuresSection) {
    featuresSection.scrollIntoView({ behavior: 'smooth' });
  }
}

// Authentication Tab Switching
function switchAuthTab(tab) {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const tabButtons = document.querySelectorAll('.tab-btn');
  
  // Remove active class from all tabs
  tabButtons.forEach(btn => btn.classList.remove('active'));
  
  if (tab === 'login') {
    loginForm.style.display = 'block';
    registerForm.style.display = 'none';
    tabButtons[0].classList.add('active');
  } else if (tab === 'register') {
    loginForm.style.display = 'none';
    registerForm.style.display = 'block';
    tabButtons[1].classList.add('active');
  }
}

// Handle Login
function handleLogin(event) {
  event.preventDefault();
  
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;
  
  // Simple validation
  if (email && password) {
    // Store user info in memory (not localStorage due to sandbox restrictions)
    window.currentUser = {
      name: 'William Li',
      email: email
    };
    
    // Navigate to dashboard
    showPage('dashboard-page');
    
    // Update user name in dashboard
    updateUserInfo();
  } else {
    alert('Please enter both email and password');
  }
}

// Handle Registration
function handleRegister(event) {
  event.preventDefault();
  
  const name = document.getElementById('register-name').value;
  const email = document.getElementById('register-email').value;
  const password = document.getElementById('register-password').value;
  const confirmPassword = document.getElementById('register-confirm').value;
  
  // Validate passwords match
  if (password !== confirmPassword) {
    alert('Passwords do not match!');
    return;
  }
  
  // Simple validation
  if (name && email && password) {
    // Store user info in memory
    window.currentUser = {
      name: name,
      email: email
    };
    
    // Navigate to dashboard
    showPage('dashboard-page');
    
    // Update user name in dashboard
    updateUserInfo();
  } else {
    alert('Please fill in all fields');
  }
}

// Update user info in dashboard
function updateUserInfo() {
  if (window.currentUser) {
    const userNameElements = document.querySelectorAll('#user-name, #profile-name');
    userNameElements.forEach(el => {
      if (el) el.textContent = window.currentUser.name;
    });
    
    const userEmailElement = document.getElementById('profile-email');
    if (userEmailElement) {
      userEmailElement.textContent = window.currentUser.email;
    }
  }
}

// Handle Logout
function handleLogout() {
  // Clear user info
  window.currentUser = null;
  
  // Navigate back to landing page
  showPage('landing-page');
  
  // Reset forms
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  if (loginForm) loginForm.reset();
  if (registerForm) registerForm.reset();
}

// Dashboard Tab Switching
function switchDashboardTab(tab) {
  // Hide all tab contents
  const tabContents = document.querySelectorAll('.tab-content');
  tabContents.forEach(content => content.classList.remove('active'));
  
  // Remove active class from all tabs
  const tabButtons = document.querySelectorAll('.dashboard-tab');
  tabButtons.forEach(btn => btn.classList.remove('active'));
  
  // Show selected tab content
  const targetTab = document.getElementById(`${tab}-tab`);
  if (targetTab) {
    targetTab.classList.add('active');
  }
  
  // Add active class to clicked tab button
  const activeButton = Array.from(tabButtons).find(btn => 
    btn.textContent.toLowerCase().includes(tab.replace('-', ' '))
  );
  if (activeButton) {
    activeButton.classList.add('active');
  }
}

// Initialize carousel animation on page load
document.addEventListener('DOMContentLoaded', function() {
  // Set default page to landing
  showPage('landing-page');
  
  // Initialize current user if needed
  if (!window.currentUser) {
    window.currentUser = null;
  }
});

// Prevent form submission defaults
document.addEventListener('submit', function(event) {
  // Let our custom handlers take care of forms
  const forms = ['login-form', 'register-form'];
  if (forms.includes(event.target.id)) {
    event.preventDefault();
  }
});