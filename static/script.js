const form = document.getElementById('challenge-form');
const result = document.getElementById('result');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const input1 = document.getElementById('input1').value.toLowerCase();
  const input2 = document.getElementById('input2').value.toLowerCase();
  const input3 = document.getElementById('input3').value.toLowerCase();
  const answer = input1.concat(input2, input3);

  if (answer === 'eggkeyboardmap') {
    window.location.href = '/challenge2';
    result.textContent = 'Correct! Proceeding to the next challenge...';
  } else {
    result.textContent = 'Incorrect. Try again!';
    result.classList.add('error');
  }
});
