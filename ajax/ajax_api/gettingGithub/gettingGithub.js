// console.log(`\n\ndocument.querySelector('#username'): \n${document.querySelector('#username').value}\n\n`);


async function githubAPI() {
    
    const input = document.querySelector('#username').value;  
    
    const response = await fetch(`https://api.github.com/users/${input}`);
    
    const apiData = await response.json();
    
    document.querySelector("p").innerText = JSON.stringify(apiData);
    
}
