// Used bootstrap v4.5,jquery v3.5.1, owl carousel v2, font awesome v4.7.0

$('.testi.owl-carousel').owlCarousel({
    items: 2,
    margin:10,
    dots:true,
    loop: true,
    
    autoplay:true,
    autoplayHoverPause:true,
    autoplayTimeout:2000,
    responsive:{
      0:{
        items:1,
      },
      600:{
        items:2,
      },
      1000:{
        items:2,
        autoplay:true,
        autoplayHoverPause:true,
        autoplayTimeout:2000,
      }
    }
  });