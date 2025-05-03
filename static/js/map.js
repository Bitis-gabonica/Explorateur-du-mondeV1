
document.addEventListener("DOMContentLoaded", function () {
    const map = new jsVectorMap({
        selector: "#world-map",
        map: "world",
        zoomButtons: true,
        onRegionClick(index, code, regionName) {
            window.location.href = `/country/${code}`;
        },
    });
});
