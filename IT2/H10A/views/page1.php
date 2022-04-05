<?php
if(isset($_COOKIE['User']))
{
    $user=unserialize($_COOKIE['User']);       

    var_dump($user);
    echo $user['Jmeno'];
     
}
?>