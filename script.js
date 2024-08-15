(function ($) {
    $(function () {
        var slider = $(".slider-moj").flickity({
            imagesLoaded: false,
            percentPosition: false,
            prevNextButtons: false, //true = enable on-screen arrows
            initialIndex: 1,
            pageDots: false, //true = enable on-screen dots
            groupCells: 1,
            selectedAttraction: 0.2,
            friction: 0.8,
            draggable: false //false = disable dragging
        });

        //this enables clicking on cards
        slider.on(
            "staticClick.flickity",
            function (event, pointer, cellElement, cellIndex) {
                if (typeof cellIndex == "number") {
                    slider.flickity("selectCell", cellIndex);
                }
            }
        );

        //this resizes the cards and centers the carousel; the latter tends to move a few pixels to the right if .resize() and .reposition() aren't used
        var flkty = slider.data("flickity");
        flkty.selectedElement.classList.add("is-custom-selected");
        flkty.resize();
        flkty.reposition();
        let time = 0;
        function reposition() {
            flkty.reposition();
            if (time++ < 10) {
                requestAnimationFrame(reposition);
            } else {
                $(".flickity-prev-next-button").css("pointer-events", "auto");
            }
        }
        requestAnimationFrame(reposition);

        //this expands the cards when in focus
        flkty.on("settle", () => {
            $(".karticka").removeClass("is-custom-selected");
            $(".flickity-prev-next-button").css("pointer-events", "none");
            flkty.selectedElement.classList.add("is-custom-selected");

            let time = 0;
            function reposition() {
                flkty.reposition();
                if (time++ < 10) {
                    requestAnimationFrame(reposition);
                } else {
                    $(".flickity-prev-next-button").css("pointer-events", "auto");
                }
            }
            requestAnimationFrame(reposition);
        });

        //this reveals the carousel when the user loads / reloads the page
        $(".carousel-moj").addClass("animation-reveal");
        $(".carousel-moj").css("opacity", "0");
        flkty.resize();
        flkty.reposition();
        setTimeout(() => {
            $(".carousel-moj").removeClass("animation-reveal");
            $(".carousel-moj").css("opacity", "1");
            flkty.resize();
            flkty.reposition();
            let time = 0;
            function reposition() {
                flkty.reposition();
                if (time++ < 10) {
                    requestAnimationFrame(reposition);
                }
            }
            requestAnimationFrame(reposition);
        }, 1000);
    });
})(jQuery);