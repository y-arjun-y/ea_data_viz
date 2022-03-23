// Sidebar and about visibility

function toggleSidebarVisible() {
  const sidebar = document.getElementById("sidebar");
  const buttress = document.getElementById("sidebar-buttress");

  if (!window.matchMedia("(max-width: 800px)").matches) {
    if (sidebar.classList.contains("toggled")) {
      sidebar.classList.remove("toggled");
      buttress.classList.remove("toggled");
      sidebar.classList.remove("toggled-mobile");
      buttress.classList.remove("toggled-mobile");
    } else {
      sidebar.classList.add("toggled");
      buttress.classList.add("toggled");
      sidebar.classList.remove("toggled-mobile");
      buttress.classList.remove("toggled-mobile");
    }
  } else {
    if (sidebar.classList.contains("toggled-mobile")) {
      sidebar.classList.remove("toggled-mobile");
      buttress.classList.remove("toggled-mobile");
    } else {
      sidebar.classList.add("toggled-mobile");
      buttress.classList.add("toggled-mobile");
    }
  }
}

function toggleAboutVisibility() {
  const about = document.getElementById("about-box");

  if (about.classList.contains("hidden")) {
    about.classList.remove("hidden");
  } else {
    about.classList.add("hidden");
  }
}

if (window.matchMedia("(max-media: 800px)").matches) {
  function mobileSidebar() {
    toggleSidebarVisible();
  }
}

// Dark mode and light mode

function setDarkMode() {
  document.body.classList.add("darkmode");
  const button = document.getElementById("darkmode-button");
  button.src = "/assets/images/ui-images/sun.svg";
  button.classList.add("noprefer");
}

function setLightMode() {
  document.body.classList.remove("darkmode");
  const button = document.getElementById("darkmode-button");
  button.src = "/assets/images/ui-images/moon.svg";
  button.classList.add("noprefer");
}

function toggleDarkMode() {
  if (document.body.classList.contains("darkmode")) setLightMode();
  else setDarkMode();
}

// Initial dark mode preference
window.onload = () => {
  if (
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
  ) {
    setDarkMode();
  }
};

// Detect changes in dark mode preferences
window.matchMedia("(prefers-color-scheme: dark)").addListener(function (e) {
  if (e.matches) setDarkMode();
  else setLightMode();
});

// Key EA numbers

document.querySelectorAll("#card-div div .question").forEach((card) => {
  card.addEventListener("click", () => {
    if (card.nextElementSibling.style.display == "none") {
      card.nextElementSibling.style.display = "block";
      card.nextElementSibling.nextElementSibling.style.display = "block";
      card.nextElementSibling.nextElementSibling.nextElementSibling.style.display =
        "block";
      card.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.style.display =
        "block";
    } else {
      card.nextElementSibling.style.display = "none";
      card.nextElementSibling.nextElementSibling.style.display = "none";
      card.nextElementSibling.nextElementSibling.nextElementSibling.style.display =
        "none";
      card.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.style.display =
        "none";
    }
  });
});

document.getElementById("sidebar").setAttribute("onclick", "mobileSidebar()");
