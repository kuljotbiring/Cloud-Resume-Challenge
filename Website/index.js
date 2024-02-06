// Javascript Code
// select the element from index.html
const counter = document.querySelector(".counter-number");
// create function which performs a fetch request to the Lambda function URL
async function updateCounter() {
	let response = await fetch("https://tzs43rorg2ll4gkthtxfifrm5a0ymlwn.lambda-url.us-east-1.on.aws/");
	// store the response in the data variable
	let data = await response.json();
	// update the counter-number variable in index.html
	counter.innerHTML = ` Views: ${data}`;
}

updateCounter();