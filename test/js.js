const accessToken =
  "yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXNhbiIsImV4cCI6MTcyMDkwMzk5NX0.ssacxcn3sxBrsYnohdSLg0FXTn1K4zF_FEaHfKL7lZ8";
fetch("http://127.0.0.1:8000/me", {
  method: "GET",
  headers: {
    Authorization: `bearer ${accessToken}`,
  },
})
  .then((response) => response.json())
  .then((data) => console.log(data));
