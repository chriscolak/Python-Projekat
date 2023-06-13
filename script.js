document.getElementById("searchButton").addEventListener("click", function () {
    var searchInput = document.getElementById("searchInput").value;
    if (searchInput.toLowerCase() === "snoop dog") {
        window.location.href = "https://en.wikipedia.org/wiki/Snoop_Dogg";
    } else if (searchInput.toLowerCase() === "madonna") {
        alert("Sorry, this can't be found.");
    }
});
