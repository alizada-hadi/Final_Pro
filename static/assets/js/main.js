const eventBox = document.getElementById("event-box")
console.log(eventBox.textContent)
const countDownBox = document.getElementById("countDown")

const eventDate = Date.parse(eventBox.textContent)

const countdown = setInterval(() => {
    const now = new Date().getTime()
    const diff = eventDate - now
    

    const day = Math.floor(eventDate / (1000*60*60*24) - (now/(1000*60*60*24)))
    const hour = Math.floor((eventDate / (1000 * 60 * 60) - (now /  (1000 * 60 * 60))) % 24)
    const minute = Math.floor((eventDate / (1000 * 60) - (now /  (1000 * 60))) % 60)
    const second = Math.floor((eventDate / (1000) - (now /  (1000))) % 60)
    if (diff > 0) {
        countDownBox.innerHTML = day + " days, "  + hour + " hours, " + minute + " minutes, " + second + " seconds "
    }
    else{
        clearInterval(countDownBox)
        countDownBox.innerHTML = "<span class='badge badge-danger badge-pill p-2'> Assignment Terminated </span>"
    }

}, 1000)


console.log("hello there")