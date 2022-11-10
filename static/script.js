const gridContainer = document.getElementById("grid-container");
const guess = document.getElementById("guess");
const clearButton = document.getElementById("clearButton");
const guessButton = document.getElementById("guessButton");
let cellData = Array(28).fill().map(() => Array(28).fill(0));
let cells;

function guessFunctionality() {
    guessButton.addEventListener("click", guessNumber);
}

function guessNumber() {
    let data = {
        data: cellData,
    }

    fetch(`${window.origin}/predict`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then(res => {
        res.json().then(data => {
            console.log(data.message);
            guess.textContent = `Your number is ${data.message}`;
        })
    })
}

function clearFunctionality() {
    clearButton.addEventListener("click", clearGrid);
}

function createGrid() {
    for (let i = 0; i < 28; i++) {
        for (let j = 0; j < 28; j++) {
            let cell = document.createElement("div");
            cell.classList.add("cell");
            let row = i.toString();
            let col = j.toString();
            let position = row + "c" +  col;
            cell.setAttribute("id", position);
            gridContainer.appendChild(cell);
        }
    }
    cells = document.querySelectorAll(".cell");
}

function clearGrid() {
    cells.forEach((cell) => {
        cell.style.backgroundColor = "white";
    });
    cellData = Array(28).fill().map(() => Array(28).fill(0));
}

function paintPixel() {
    let cell = document.getElementById(this.id);
    cell.style.backgroundColor = "black";
    let pos = this.id.split("c");
    let row = pos[0];
    let col = pos[1];
    cellData[row][col] = 1;
}

function drawing() {
    gridContainer.addEventListener("mousedown", allowDrawing);

    gridContainer.addEventListener("mouseup", disableDrawing);

    gridContainer.addEventListener("mouseleave", disableDrawing);
}

function allowDrawing() {
    cells.forEach((cell) => {
        cell.addEventListener("mouseover", paintPixel);
    });
}

function disableDrawing() {
    cells.forEach((cell) => {
        cell.removeEventListener("mouseover", paintPixel);
    });
}

createGrid();
drawing();
clearFunctionality();
guessFunctionality();
