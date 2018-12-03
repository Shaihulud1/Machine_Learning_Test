<?php
if(isset($_POST['save']))
{
    $data = trim(htmlspecialchars($_POST['save']));
    $file = isset($_POST['save']) ? trim(htmlspecialchars($_POST['file'])) : 'resultJson';
    file_put_contents($file.'.json', $data);
}
