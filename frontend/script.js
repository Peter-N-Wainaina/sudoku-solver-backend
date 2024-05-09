document.addEventListener('DOMContentLoaded', function () {
    const board = document.getElementById('sudoku-board');
    var board_size = 9;
    for (let i = 0; i < board_size; i++) {
        const row = document.createElement('div');
        for (let j = 0; j < board_size; j++) {
            const input = document.createElement('input');
            input.type = 'text';
            input.maxLength = '1';
            input.oninput = function() { validateInput(this); };
            row.appendChild(input);
        }
        board.appendChild(row);
    }

    // Adding event listener to the Solve button
    document.getElementById('solve-button').addEventListener('click', function() {
        alert('Solve Sudoku button clicked!'); // Placeholder for actual solve logic
    });
});

function validateInput(input) {
    input.value = input.value.replace(/[^1-9]/g, '');
}
