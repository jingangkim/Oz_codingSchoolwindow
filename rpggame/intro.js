const buttons = document.querySelectorAll('button');
const descriptions = document.querySelectorAll('.description');

buttons.forEach((button, index) => {
    button.addEventListener('click', () => {
        // 모든 description을 숨김
        descriptions.forEach(desc => desc.style.display = 'none');
        // 클릭한 버튼에 해당하는 description만 보임
        descriptions[index].style.display = 'block';
    });
});

const form = document.getElementById('class_pick');

form.addEventListener('submit', (event) => {
const radioButtons = form.querySelectorAll('input[type="radio"]');
let selected = false;

radioButtons.forEach((radioButton) => {
    if (radioButton.checked) {
    selected = true;
    }
});

if (!selected) {
    event.preventDefault();
    alert('직업을 선택해주세요.');
}
});