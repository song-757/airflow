FRUIT=$1
if [ $FRUIT == APPLE ] ; then
        echo "You selected Apple"
elif [ $FRUIT == ORANGE ] ; then
        echo "You selected Orange"
elif [ $FRUIT == GRAPE ] ; then
        echo "You selected Graph"
else
        echo "You selected Other Fruit"
fi