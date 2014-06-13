

    $(".form_control[name='quantity']").TouchSpin({
        initval: 1
    });
    $("#tab").tabs();
    $(".product .size ul li span.active").click(function(){
        var stock = parseInt($(this).attr("stock"));
        $(".product .size ul li span.active").removeClass("select");
        $(this).addClass("select");
    });

    $(".thumb").mouseover(function(){
        var url = $(this).attr("src").split("-middle")[0];
        $(".cover>a").attr("href",url);
        url+="-big";
        $(".cover>a>img").attr("src",url);
    });

    $(".cart_btn a").click(function(){
        var href="/cart/add/";
        if ($(".size ul li .select").length == 0)
          $(".error_message").slideDown();
        else{
          $(".error_message").slideUp();
          href+="?pid="+$(".product").attr("data_value")+"&quantity="+$("#id_quantity").val()
            +"&color="+$(".color>li").attr("option_value")
            +"&size="+$(".size ul>li>.select").parent().attr("option_value")+"&cid="+$(this).attr("data_value");
          window.location.href=href;
        }
    });

