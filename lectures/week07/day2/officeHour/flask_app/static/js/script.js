console.log("we are all connected")

function counter(a) {
    var count = document.getElementById(a)
    console.log(count)
    var num = parseInt(count.innerText)
    num++
    console.log(num)
    count.innerText = num
}
