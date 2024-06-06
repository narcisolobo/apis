const jokeContainer = document.getElementById('joke-container');

function waitASec() {
  setTimeout(function () {
    console.log('Hello');
  }, 1000);
  console.log('Goodbye');
}

waitASec();

async function getDadJoke() {
  const myHeaders = new Headers();
  myHeaders.append('Accept', 'application/json');
  const response = await fetch('https://icanhazdadjoke.com/', {
    headers: myHeaders,
  });

  const joke = await response.json();

  jokeContainer.textContent = joke.joke;
}

getDadJoke();
