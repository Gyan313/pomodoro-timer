const timer = {
  Pomodoro: dataFromDatabase[0].fields.pomodoro,
  shortBreak: dataFromDatabase[0].fields.short_break,
  longBreak: dataFromDatabase[0].fields.long_break,
  autoStartPomodoros: dataFromDatabase[0].fields.auto_start_pomodoros,
  autoStartBreaks: dataFromDatabase[0].fields.auto_start_breaks,
  longBreakIntervals: dataFromDatabase[0].fields.number_of_interval,
  sessions: 0,
};

// for manually testing
/* const timer = {
  Pomodoro: 1,
  shortBreak: 1,
  longBreak: 1,
  autoStartPomodoros: true,
  autoStartBreaks: true,
  longBreakIntervals: 1,
  sessions: 0,
}; */

let interval;
const modeButtons = document.getElementById("js-mode-buttons");
modeButtons.addEventListener("click", handlemode);

let progressBar = document.getElementById("js-progress-bar");

function switchMode(mode) {
  timer.mode = mode;
  timer.remainingTime = {
    total: timer[mode] * 60,
    minutes: timer[mode],
    seconds: 0,
  };

  document
    .querySelectorAll("button[data-mode]")
    .forEach((e) => e.classList.remove("active"));
  document.querySelector(`[data-mode = "${mode}"]`).classList.add("active");
  document.body.style.backgroundColor = `var(--${mode})`;

  progressBar.setAttribute("max", `${timer.remainingTime.total}`);

  updateClock();
}

function updateClock() {
  const { remainingTime } = timer;
  const minutes = `${remainingTime.minutes}`.padStart(2, "0");
  const seconds = `${remainingTime.seconds}`.padStart(2, "0");

  const min = document.getElementById("js-minutes");
  const sec = document.getElementById("js-seconds");
  min.innerHTML = minutes;
  sec.innerHTML = seconds;

  // putting the pomodoro in the title of the page.
  const titleText =
    timer.mode === "Pomodoro" ? "Focus On Work" : "Take A Break";
  document.querySelector(
    "title"
  ).innerHTML = `${minutes}:${seconds} - ${titleText}`;
}

let mainButton = document.querySelector(".submit-button");
mainButton.addEventListener("click", () => {
  const { action } = mainButton.dataset;
  if (action == "start") {
    startTimer();
  } else {
    stopTimer();
  }
});

// function to play sound after breaks and pomodoros ends
function playsound(audio_tag_id){
  let audio_element = document.querySelector(`#${audio_tag_id}`)
    audio_element.load()
    audio_element.play()
    setTimeout(() => {
      audio_element.pause();
    }, 5000);
}

// Logic of startTimer:
/* 1) Look at the maths in getRemainingTime(endpoint) function which you can easily understand.
   2) only thing you need to understand is that, I needed a time quantity which is changing every
      second. And that is now() time. And i need this quantity inside the setInterval() function.
   3) But I also need a "endpoint" which I am getting by doing now() + (total minutes) input by   user.
*/
function startTimer() {
  let { total } = timer.remainingTime;
  const endpoint = new Date().getTime() + total * 1000;

  // not putting the progress-bar here because for this bar we only want total time the timer
  // is supposed to be done in. Not the actuall time at which timer is to stop.

  // if we cycle back to pomodoro just increment the sessions as we still havent reached the
  // longBreakInterval.
  if (timer.mode == "Pomodoro") {
    timer.sessions++;
  }

  // when someone click on the button while timer is running.
  mainButton.dataset.action = "stop";
  mainButton.innerHTML = "Squash";
  mainButton.classList.add("active");

  interval = setInterval(() => {
    timer.remainingTime = getRemainingTime(endpoint);
    updateClock();

    total = timer.remainingTime.total;

    // updating the value of progress-bar
    progressBar.setAttribute("value", `${timer[timer.mode] * 60 - total}`);

    if (total <= 0) {
      clearInterval(interval);

      switch (timer.mode) {
        case "Pomodoro":
          playsound("pomodoro-audio")
          if (timer.sessions % timer.longBreakIntervals == 0) {
            switchMode("longBreak");
          } else {
            switchMode("shortBreak");
          }
          if (timer.autoStartBreaks) {
            startTimer();
          }
          break;
        case "longBreak":
          stopTimer();
          playsound("break-audio")
          switchMode("Pomodoro");
          break;
        default:
          playsound("break-audio")
          switchMode("Pomodoro");
          if (timer.autoStartPomodoros) {
            startTimer();
          }
      }
    }
  }, 1000 / 60);
}

function stopTimer() {
  clearInterval(interval);

  mainButton.dataset.action = "start";
  mainButton.innerHTML = "Wind Up";
  mainButton.classList.remove("activate");
}

document.addEventListener("DOMContentLoaded", () => {
  switchMode("Pomodoro");
});

function getRemainingTime(endpoint) {
  let difference = endpoint - new Date().getTime();

  let total = Number.parseInt(difference / 1000, 10);
  let minutes = Number.parseInt(difference / (1000 * 60), 10);
  let seconds = Number.parseInt((difference / 1000) % 60, 10);

  return {
    total,
    minutes,
    seconds,
  };
}

function handlemode(event) {
  const { mode } = event.target.dataset;
  if (!mode) return;
  switchMode(mode);
  stopTimer();
}

// js for task list
// 1) When clicked on checkbox, the text should be crossed over by a line.
// 2) When clicked on delete button, the text should be removed from the list not from the database.
      // 2) Delete button is on timer.html page

// 1) Done
// got all the checkedTasks
const checkedTasks = document.querySelectorAll('input[name="task-list"]'); 
checkedTasks.forEach((checkbox)=>{
  // "input" is the event-listener for <input> tag.So, "click" and "change" these dont work.
  checkbox.addEventListener("input",()=>{
    let task_id = checkbox.id;
    let labelAssociated = document.querySelector(`label[for='${task_id}']`)
    if(checkbox.checked){
      labelAssociated.innerHTML = `<s>${labelAssociated.textContent}</s>`
      // using ajax to send the id of the checked task so that i can get end-time of the task.
      notify_database(checkbox.dataset.taskid,1);
    }
    else{
      labelAssociated.innerHTML = `<strong>${labelAssociated.textContent}</strong>`;
      notify_database(checkbox.dataset.taskid,0);
    }
  })
})

function notify_database(checkboxTaskId,is_checked){
  $.ajax({
    type:"GET",
    url: "/Pomodoro_App/timer/",
    data:{
      task_id:checkboxTaskId,
      checked:is_checked
    },
    success:()=>{
      console.log("it happened")
    },
  })
}

// creating clock for which shows actual time.
// https://codepen.io/kylewetton/pen/QJbOjw
