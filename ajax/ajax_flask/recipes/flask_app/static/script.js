const emailRegex = new RegExp("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$");

const register = document.querySelector("form");

register.onsubmit = function validateRegistration(e) {
    
    e.preventDefault();
    
    const registerData = Object.fromEntries(new FormData(document.querySelector("form")));
    
    var messages = document.createElement("p");
    
    isValid = true;
    
    if (registerData.first_name.length < 2) {
        
        messages.innerHTML += "<br><br> First Name must be at least 2 characters long";
        
        isValid = false;
        
    }
    
    if (registerData.last_name.length < 2) {
        
        messages.innerHTML += "<br><br> Last Name must be at least 2 characters long";
        
        isValid = false;
        
    }
    
    if (!emailRegex.test(registerData.email)) {
        
        messages.innerHTML += "<br><br> You have entered an invalid email address";
        
        isValid = false;
        
    }
    
    if (registerData.email !== registerData["confirm-email"]) {
        
        messages.innerHTML += "<br><br> The two emails you entered did not match";
        
        isValid = false;
        
    }
    
    fetch("http://localhost:5000/get-emails", { method : "GET" })
    .then(response => response.json())
    .then(data => { if (data.indexOf(registerData.email) !== -1) { 
        
                messages.innerHTML += "<br><br> This email address has already been registered foo!";
                
                isValid = false;; 
                
                }
            }
        );
        
    if (registerData.password !== registerData["confirm-password"]) {
        
        messages.innerHTML += "<br><br> The two passwords do not match";
        
        isValid = false;
        
    }                
 
    document.body.appendChild(messages);
    
    if (isValid === true) {
        
        var form = new FormData(register)
        
        fetch("http://localhost:5000/register", { method : "POST", body : form });
        
    }
    
}

const login = document.querySelector("#login");

login.onsubmit = function validateLogin(e) {
    
    e.preventDefault();
    
    const loginData = Object.fromEntries(new FormData(document.querySelector("#login")));
    
    var messages = document.createElement("p");
    
    isValid = true;
    
    if (!emailRegex.test(loginData["login-email"])) {
        
        messages.innerHTML += "<br><br> You have entered an invalid email address";
        
        isValid = false;
        
    }
    
    fetch("http://localhost:5000/get-emails", { method : "GET" })
    .then(response => response.json())
    .then(data => { if (data.indexOf(loginData["login-email"]) === -1) { 
        
                messages.innerHTML += "<br><br> This email address has not been registered foo!";
                
                isValid = false;
                
                }
            }
        );                          
 
    document.body.appendChild(messages);
    
    if (isValid === true) {
        
        var form = new FormData(login)
        
        fetch("http://localhost:5000/login", { method : "POST", body : form })
        
    }
    
}