const modalBtns = [...document.getElementsByClassName("modal-button")]
const modalBody = document.getElementById("modal-body")
modalBtns.forEach(modalBtn=>modalBtn.addEventListener("click", () => {
    const pk = modalBtn.getAttribute("data-pk")
    const title = modalBtn.getAttribute("data-event")
    const start_time = modalBtn.getAttribute("data-start_time")
    const end_time = modalBtn.getAttribute("data-end_time")
    const course = modalBtn.getAttribute("data-course")
    const description = modalBtn.getAttribute("data-description")
    


    modalBody.innerHTML = `
        <h2 class='mb-2'>${title}</h2>
        <div class='row mt-3'>
            <div class="col-lg-6">
                <h6>Start Time</h6>
                <span class="" style="color: red;">
                    ${start_time}
                </span>
            </div>
            <div class="col-lg-6">
                <h6>Ent Time</h6>
                    <span class="" style="color: red;">
                        ${end_time}
                    </span>
            </div>
        </div>

        <div class="mt-3">
            <h6>Participants</h6>
            <span class="badge badge-default p-2 font-size-16" style="border: 1px solid gray;">
            ${course}
            </span>
        </div>

        <div class="mt-3">
            <h6>Description</h6>
            ${description}
        </div>
    
    `

}))