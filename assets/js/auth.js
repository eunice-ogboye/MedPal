document.addEventListener("DOMContentLoaded", function () {
    const menuBar = document.querySelector(".menu-bar");
    const menuList = document.querySelector(".menu ul");

    menuBar.addEventListener("click", function () {
      menuList.style.display =
        menuList.style.display === "flex" ? "none" : "flex";
    });
  });
  const token = localStorage.getItem("accessToken"); // Retrieve token from local storage

  const isLoggedIn = !!token; // Check if a token exists

  // Check if the user is logged in (You might have a different way to check this)

  const assessmentLink = document.getElementById("assessmentLink");

  if (!isLoggedIn) {
    // If the user is not logged in, route to the sign-in page
    assessmentLink.href = "./pages/signin.html";
  } else {
    // If the user is logged in, route to the chat page
    assessmentLink.href = "./pages/chat.html";
  }