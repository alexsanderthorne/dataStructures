import java.util.Arrays;

class Main {

  public static void selectionSort(int[] array) {
    for (int fixo = 0; fixo < array.length - 1; fixo++) {
      int menor = fixo;

      for (int i = menor + 1; i < array.length; i++) {
        if (array[i] < array[menor]) {
          menor = i;
        }
      }
      if (menor != fixo) {
        int t = array[fixo];
        array[fixo] = array[menor];
        array[menor] = t;
      }
    }
    System.out.println(Arrays.toString(array));
  }

  public static void main(String[] args) {

    int[] array = { 2, 4, 3, 77, 6, 9 };

    selectionSort(array);

  }
}