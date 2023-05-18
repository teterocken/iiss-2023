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
