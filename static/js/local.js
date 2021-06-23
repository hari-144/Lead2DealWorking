var filename = "";
var loadStatus = false;
var ctx;
var currentImage = "";

$(document).ready(function(){
    loadStatus = false;
    ctx = false;
    $("#wait_element").hide();
})





function load_page(data){
   
    var img = new Image();
    var canvas = document.getElementById("page");
    var context = canvas.getContext("2d");
        
    

    context.clearRect(0, 0, 660, 760);
    img.src = 'http://127.0.0.1:9090/static/processed_images/'+data+'.jpg';
    currentImage = 'http://127.0.0.1:9090/static/processed_images/'+data+'.jpg';
    
    img.onload = function(){
        context.drawImage(img, 0, 0, 660, 760);
    }
    loadStatus = true;
    ctx = context;
    $("#currentPage").val(data);
    $("canvas").css("overflow", "scroll");
}

function setFileName(fName){
    document.getElementById("pageImages").innerHTML = "";
    filename = fName;
    loadStatus = false;
    ctx = false;
    var send_data = JSON.stringify({"file_name": ""+ filename +""});
    // $("#wait_element").show();
    
    $.ajax({
        type: "POST",
        url: "/process_pdf",
        contentType: "application/json",
        data: send_data,
        beforeSend: function(){
            
            $("#wait_element").show();
        },
        success: function(response){
            // alert(response)
            var starter = "<ul class='list-group list-group-flush'>";
            var pageInfo = ""
            for(var pageIndex=0; pageIndex < response["data"].length;pageIndex++){
                pageInfo+="<li class='list-group-item'><a href='javascript:void' class='text-danger' onclick='load_page(\""+ response["data"][pageIndex]["file_name"] +"\")'>"+response["data"][pageIndex]["file_name"]+"</a></li>";
            }
            pageInfo = starter + pageInfo + "</ul>";

            document.getElementById("pageImages").innerHTML = pageInfo;
            $("#wait_element").hide();
        },
        complete: function(data){
            $("#wait_element").hide();
        }
    })
}
