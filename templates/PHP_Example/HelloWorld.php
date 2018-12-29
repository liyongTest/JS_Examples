<!DOCTYPE html>
<html>
<body>

<h1>My first PHP page</h1>
    <?php
        echo "HelloWorld"
    ?>
    <?php
        $x=5;
        $y=6;
        $z=$x+$y;
        echo $z;
        echo "<br>"
    ?>
    <?php
        define("GREETING","Welcome to my page!");
        echo GREETING
    ?>
</body>
</html> 

