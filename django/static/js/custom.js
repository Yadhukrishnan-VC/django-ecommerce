$(document).ready(function(){

    $('.increment-btn').click(function (e){
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
        if (value < 10);
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e){
        e.preventDefault();
    
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if (value > 1);
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.AddToCartBtn').click(function (e){
        e.preventDefault();
    
        var product_id = $(this).closest('product_data').find('.prod_id').val();
        var product_qty = $(this).closest('product_data').find('.qty-input').val();
        token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: "/add-to-cart",
            data: {
                'product_id' : product_id,
                'product_qty' : product_qty,
                csrfmiddlewaretoken : token
            },
            dataType: "dataType",
            success: function (response) {
                
            }
        });
    });

});


