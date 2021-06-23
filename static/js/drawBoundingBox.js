var canvas = document.getElementById("page");
var context = canvas.getContext("2d");
var canvas_x = $(canvas).offset().left;
var canvas_y = $(canvas).offset().top;
var mouse_x = mouse_y = 0;
var last_x = last_y = 0;
var mopuse_down = false;


// Mouse down event def

$(canvas).on("mousedown", function(event){
    last_x = parseInt(event.clientX - canvas_x);
    last_y = parseInt(event.clientY - canvas_y);
    mouse_down = true;
});

// Mouse up event def

$(canvas).on("mouseup", function(event){
    mouse_down = false;
});

// Mouse move event
// Mouse down event def

$(canvas).on("mousemove", function(event){
    mouse_x = parseInt(event.clientX - canvas_x);
    mouse_y = parseInt(event.clientY - canvas_y);
    if (mouse_down == true){
        context.beginPath();
        var width = mouse_x - last_x;
        var height = mouse_y - last_y;
        context.rect(last_x, last_y, width, height);
        context.strokeStyle  = "green";
        context.lineWidth  = 2;
        context.stroke();
    }
    alert("Mouse X" + mouse_x + "Mouse Y" + mouse_y + "End X" + last_x + "End_Y" + last_y);
    // mouse_down = true;
});