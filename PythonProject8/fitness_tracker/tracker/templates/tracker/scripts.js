function filterCategory(category) {
    let workouts = document.querySelectorAll(".workout");
    workouts.forEach(workout => {
        if (category === "all" || workout.classList.contains(category)) {
            workout.style.display = "block";
        } else {
            workout.style.display = "none";
        }
    });
}

function filterWorkouts() {
    let searchValue = document.getElementById("search").value.toLowerCase();
    let workouts = document.querySelectorAll(".workout h2");

    workouts.forEach(workout => {
        let parent = workout.parentElement;
        if (workout.innerText.toLowerCase().includes(searchValue)) {
            parent.style.display = "block";
        } else {
            parent.style.display = "none";
        }
    });
}
