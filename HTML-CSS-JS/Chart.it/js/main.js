let canvas = document.getElementsByTagName("canvas")[0];
canvas.width = 600;
canvas.height = 400;
let ctx = canvas.getContext("2d");
let xGrid = 10;
let paddingLeft = 20;
let paddingBottom = 20;
let chartHight = canvas.height - paddingBottom;
// Path begin for chart rectangle.
ctx.beginPath();
ctx.strokeStyle = "rgb(0,0,0)";
ctx.rect(paddingLeft, 0, canvas.width - paddingLeft, chartHight);
ctx.stroke();
ctx.closePath();
// Path begin for horizontal grid lines.
ctx.beginPath();
ctx.strokeStyle = "rgba(0,0,0,0.5)";
while (xGrid < chartHight) {
  ctx.moveTo(paddingLeft, xGrid);
  ctx.lineTo(canvas.width, xGrid);
  xGrid += 10;
}
ctx.stroke();
ctx.closePath();