jQuery(document).ready( function($) {
	

 $( "input[name^='paidamt']").keyup(function() {
	 
	 $(this).css({
                    "border": "",
                    "background": ""
                });
	 matchfee = Math.round($('#matchamt').text());
	 var ePaidamt = $(this);
	 paidamt = (isNaN(ePaidamt.val())) ? 0 : ePaidamt.val();
	 //debugger;
	 var paidid = this.id;
	 paidid = paidid[paidid.length -1];
	 creditamtId = "creditamt" + paidid;
	 //creditamt =  parseInt($('#' + creditamtId).text());
	 
	 $.ajax({
        url: '/ypf/ajax/get_credit/',
        data: {
          'playerid': paidid
        },
        dataType: 'json',
        success: function (data) {
         if(paidamt != 0)
		 creditamt = data.creditamt - (matchfee - paidamt);
	 else
		 creditamt = data.creditamt;
	     $('#' + creditamtId).val(creditamt);
	      
        }
      });
	});
	
	/* $("form").submit(function() {
     
      alert('valid');
	  return false;
    }); */
	$('#btnSubmit').click(function(e) {
        var isValid = true;
        $('input[type="text"]').each(function() {
	if ($.trim($(this).val()) == '' || isNaN($(this).val()) ) {
                isValid = false;
                $(this).css({
                    "border": "1px solid red",
                    "background": "#FFCECE"
                });
            }
            else {
                $(this).css({
                    "border": "",
                    "background": ""
                });
            }
        });
        if (isValid == false) 
            e.preventDefault();
        else 
            alert('Thank you for submitting');
	})
});

