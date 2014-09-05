MouseEventDispatch = function(){
    }

MouseEventDispatch.prototype = {
    start: function(){

        _Main.canvas.onmousedown = function(event){
            g_MouseMgr.mouseDown(event);
        };
        _Main.canvas.onmousemove = function(event){
            g_MouseMgr.mouseMove(event);
        };
        var again = document.getElementById("try_again");
        again.onmousedown = function(event){
            _Main.again()
        };
    },

    end: function(){
        _Main.canvas.onmousedown = function(event){};
        _Main.canvas.onmousemove = function(event){};
    }
}