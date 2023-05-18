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
