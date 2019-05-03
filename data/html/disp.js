$(function(){
    $('#greet').on("change",function(){
        let param = { "opt": $(this).val() };
        $.post({
            url: "get.php",
            data: param,
            dataType: "json",
        }).done(function(data){
           $("#first").text(data.output_text);
        }).fail(function(XMLHttpRequest, textStatus, errorThrown){
            alert(errorThrown);
        });
    });
    $('#world').on("click",function(){
        let param = { "opt": "World!" };
        $.post({
            url: "get.php",
            data: param,
            dataType: "json",
        }).done(function(data){
           $("#second").text(data.output_text);
        }).fail(function(XMLHttpRequest, textStatus, errorThrown){
            alert(errorThrown);
        });
    });
    $('#everyone').on("click",function(){
        let param = { "opt": "みなさん" };
        $.post({
            url: "get.php",
            data: param,
            dataType: "json",
        }).done(function(data){
           $("#second").text(data.output_text);
        }).fail(function(XMLHttpRequest, textStatus, errorThrown){
            alert(errorThrown);
        });
    });
    $('#japan').on("click",function(){
        let param = { "opt": "日本" };
        $.post({
            url: "get.php",
            data: param,
            dataType: "json",
        }).done(function(data){
           $("#second").text(data.output_text);
        }).fail(function(XMLHttpRequest, textStatus, errorThrown){
            alert(errorThrown);
        });
    });
});
