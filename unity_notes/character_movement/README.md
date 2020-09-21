```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    // Start is called before the first frame update
    public float moveSpeed;
    public CharacterController playerCtrl;
    protected Vector3 move;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // get keyboard input and move object
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        move = transform.right * h + transform.up * v;
        playerCtrl.Move(move * moveSpeed * Time.deltaTime);
        
    }
}

```



```c#
public float moveSpeed;
void Update(){
  float h = Input.GetAxis("Horizontal");
  float v = Input.GetAxis("Vertical");
  transform.Translate(Vector3.right * h * moveSpeed * Time.deltaTime, Space.World);
  transform.Translate(Vector3.up * v * moveSpeed * Time.deltaTime, Space.World);
  
}
```

