// Retrieve user data from local storage
const storedUserData = localStorage.getItem('userData');
const userData = storedUserData ? JSON.parse(storedUserData) : null;

// Use the retrieved user data
if (userData) {
  // Access individual properties
  const userName = userData.email;
  const userPicture = userData.profile_picture;

  // Update elements if they exist
  const userNameElement = document.getElementById('userName');
  const userPictureElement = document.getElementById('userPicture');

  if (userNameElement) {
    userNameElement.textContent = userName || 'No Name';
  }

  if (userPictureElement) {
    userPictureElement.src = userPicture || 'placeholder.jpg';
  }
} else {
  // Handle case where user data is not available or not logged in
}
