import java.util.Arrays;

class Main {

  public static void insertionSort(int[] vetor){
		
		for (int i = 1; i < vetor.length; i++){
			
			int aux = vetor[i];
			int j = i;
			
			while ((j > 0) && (vetor[j-1] > aux)){
				vetor[j] = vetor[j-1];
				j -= 1;
			}
			vetor[j] = aux;
      System.out.println(Arrays.toString(vetor));

		}
	
	}
  public static void main(String[] args) {

    int [] vetor = {2,3,5,4,6,5,79,8,4,1};
    insertionSort(vetor);
    
  }
}