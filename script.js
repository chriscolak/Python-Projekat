document.getElementById("searchButton").addEventListener("click", function () {
    var searchInput = document.getElementById("searchInput").value;
    if (searchInput.toLowerCase() === "madonna") {
        window.location.href = "https://en.wikipedia.org/wiki/Madonna";
    } else if (searchInput.toLowerCase() === "snoop dogg") {
        window.location.href = "https://en.wikipedia.org/wiki/Snoop_Dogg";
    } else {
        alert("Sorry, this can't be found.");
    }
});
