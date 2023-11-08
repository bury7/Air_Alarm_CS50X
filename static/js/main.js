let isFetchingData = false;

// Fetching json data from API and update DOM
async function fetchDataFromAPI() {
  if (isFetchingData) {
    return;
  }

  try {
    isFetchingData = true;
    const response = await fetch('/api');
    const data = await response.json();

    for (const [key, value] of Object.entries(data)) {
      const pathId = `${key}Path`;
      const menuId = `${key}Menu`;
      const pathElement = document.getElementById(pathId);
      const menuElement = document.getElementById(menuId);
      const menuList = document.getElementById('menu-list');

      if (value.alarm) {
        if (pathElement) {
          // Update alarm in path 
          pathElement.classList.add('air-alarm');
          console.log("Information Successfully updated");
        }

        // Update alarm in right menu 
        if (!menuElement)
        {
          const newLi = document.createElement('li');
          const newA = document.createElement('a');
          const newH3 = document.createElement('h3');
          const newP_1 = document.createElement('p');
          const newP_2 = document.createElement('p');
          newA.id = menuId;
          newH3.textContent = value["eng_name"];
          newP_1.textContent = "Start: " + value["time"];
          newP_2.textContent = "Duration: " + value["duration"];
          newA.appendChild(newH3);
          newA.appendChild(newP_1);
          newA.appendChild(newP_2);
          newLi.appendChild(newA);
          menuList.appendChild(newLi);
        }
        else {
          // Update alarm duration in right menu
          var secondP = menuElement.getElementsByTagName("p")[1];
          secondP.textContent = "Duration: " + value["duration"];
        }

      } else {
        if (pathElement) {
          // Delete alarm from path 
          pathElement.classList.remove('air-alarm');
        }

        if (menuElement) {
          // Delete alarm from right menu
          menuElement.parentNode.remove()
        }
      }
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    isFetchingData = false;
  }
}

// Handles all button clicks on the site
document.addEventListener('DOMContentLoaded', function() {
  fetchDataFromAPI();
  checkTheme();

  const reloadIcon = document.querySelector('.fa-sync-alt');
  if (reloadIcon) {
    reloadIcon.addEventListener('click', fetchDataFromAPI);
  }

  const themeIcon = document.querySelector('#theme');
  if (themeIcon) {
    themeIcon.addEventListener('click', changeTheme);
  }

  const infoIcon = document.querySelector('.fa-info-circle');
  if (infoIcon) {
    infoIcon.addEventListener('click', togglePopup);
  }

  const closePopupButton = document.getElementById('closePopup');
  if (closePopupButton) {
    closePopupButton.addEventListener('click', togglePopup);
  }
  
  const menuButton = document.querySelector('.fa-bars');
  if (menuButton){
    menuButton.addEventListener('click', toggleRightMenu);
  }

  const closemenuButton = document.querySelector('.close-menu');
  if (closemenuButton){
    closemenuButton.addEventListener('click', toggleRightMenu);
  }  
});


// Manages popup
const popup = document.querySelector('.popup');
function togglePopup() {
  if (popup.classList.contains('open-popup')) {
    closePopup();
  } else {
    openPopup();
  }
}

function openPopup() {
  popup.classList.add('open-popup');
}

function closePopup() {
  popup.classList.remove('open-popup');
}

// Manages right menu
const rightMenu = document.querySelector('.right-menu');
function toggleRightMenu() {
  if (rightMenu.classList.contains('open-menu')) {
    closeRightMenu();
  } else {
    openRightMenu();
  }
}

function openRightMenu() {
  rightMenu.classList.add('open-menu');
}

function closeRightMenu() {
  rightMenu.classList.remove('open-menu');
}

// Manages dark mode
const icon = document.querySelector('#theme');
function changeTheme() {
  if (darkMode){
    darkMode = false
    document.body.classList.remove('dark');
  }
  else {
    darkMode = true
    document.body.classList.toggle('dark');
  }
  if (icon.classList.contains('fa-sun')) {
    icon.classList.remove('fa-sun');
    icon.classList.add('fa-moon');
  } else {
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
  }
}

// Check for default theme
function checkTheme() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    darkMode = true
    document.body.classList.toggle('dark');
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
} else {
    darkMode = false
    document.body.classList.remove('dark');
    icon.classList.remove('fa-sun');
    icon.classList.add('fa-moon');
}
}


setInterval(fetchDataFromAPI, 5000);
