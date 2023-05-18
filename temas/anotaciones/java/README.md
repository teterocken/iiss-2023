# Ejecución del código

Hay que situarse en la misma carpeta que todos los archivos .java y ejecutar las siguientes órdenes:

```
javac *.java
java PruebaZumo
```

# Explicación del código

La base del código es la siguiente interfaz Fruta:

```java
public interface Fruta 
{
    public void sabor ();
    public void color ();
    public void precio ();
}
```

Después se crea el siguiente codigo para poder asignar un tipo de fruta mediante anotaciones:

```java
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

@Retention(java.lang.annotation.RetentionPolicy.RUNTIME)
@Target({java.lang.annotation.ElementType.TYPE})
public @interface TipoFruta {
    Class<?> value();
}
```

Sumado a esto:

```java
public class GetFruta
{
    public Fruta getFruta(Object o) throws Exception
    {
        Class<?> c = o.getClass();
        TipoFruta tipofruta = c.getAnnotation(TipoFruta.class);
        Class<?> clasefruta = tipofruta.value();
        Fruta fruta = null;
        try
        {
            fruta = (Fruta) clasefruta.getDeclaredConstructor().newInstance();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        return fruta;
    }
}
```

Se hace realmente sencilla la inyección de dependencias a partir de anotaciones una vez tenemos esto. Primero crearemos dos tipos de fruta que implementan los métodos de la interfaz Fruta:

```java
public class Naranja implements Fruta
{
    public void sabor ()
    {
        System.out.println("Tiene un sabor acido");
    }
    public void color ()
    {
        System.out.println("Tiene un color naranja");
    }
    public void precio ()
    {
        System.out.println("Tiene un precio moderado");
    }
}
```

```java
public class Platano implements Fruta
{
    public void sabor ()
    {
        System.out.println("Tiene un sabor dulce");
    }
    public void color ()
    {
        System.out.println("Tiene un color amarillo");
    }
    public void precio ()
    {
        System.out.println("Tiene un precio bajo");
    }
}
```

Teniendo esto, se podría asignar a una clase Zumo la fruta de la que se desea hacer el zumo, el zumo tendrá las caraterísticas de la fruta, por lo que delega sus métodos en la fruta:

```java
@TipoFruta(Platano.class)
public class Zumo {
    private Fruta fruta;
    private GetFruta gf;

    public Zumo () throws Exception
    {
        gf = new GetFruta();
        fruta = gf.getFruta(this);
    }

    public void sabor ()
    {
        fruta.sabor();
    }

    public void color ()
    {
        fruta.color();
    }

    public void precio ()
    {
        fruta.precio();
    }
}
```

En este caso, como se le ha pasado la anotación con la clase Platano, se creará un zumo de platano cada vez que se desee crear un zumo, véase el siguiente ejemplo:

```java
public class PruebaZumo 
{
    public static void main (String args[]) throws Exception
    {
        Zumo zumito = new Zumo();
        zumito.sabor();
        zumito.color();
        zumito.precio();
    }
}
```

El cual dará la siguiente salida:

```
Tiene un sabor dulce
Tiene un color amarillo
Tiene un precio bajo
```

Sin embargo, si se hubiese escrito la siguiente anotación en lugar de Platano.class:

```java
@TipoFruta(Naranja.class)
```

La salida hubiese sido la siguiente:

```
Tiene un sabor acido
Tiene un precio moderado
Tiene un color naranja
```

# Conclusión
Podemos contemplar como, tan solo con cambiar la clase de la que dependerá Zumo en la anotación, podemos cambiar la inyección de dependencias (o el sabor del zumo) con tan solo cambiar el nombre de la clase.

La inyección de dependencias mediante anotaciones permite implementar ejemplos tan sencillos de una manera mucho más sencilla y versátil que en el caso de Spring Framework, sin embargo, no es la opción que elegiría para un proyecto relativamente grande.
