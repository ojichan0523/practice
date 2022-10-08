const onClickAdd = () => {
  // テキストボックスの値を取得し、初期化する
  const inputText = document.getElementById('add-text').value
  document.getElementById('add-text').value = ''

  createIncompleteList(inputText)
}

//　削除ボタン
const deleteFrom = (target) => {
  document.getElementById('incomplete-list').removeChild(target)
}

// 未完了のリストに追加する関数
const createIncompleteList = (text) => {
  // divタグを生成
  const div = document.createElement('div')
  div.className = 'list-row'

  // pタグを生成
  const p = document.createElement('p')
  p.className = 'list-title'
  p.innerText = inputText

  document.getElementById('incomplete-list').appendChild(div)

  // 完了ボタン追加
  const completeButton = document.createElement('button')
  completeButton.innerText = '完了'
  completeButton.addEventListener('click', () => {
    deleteFrom(completeButton.parentNode)
    const addTarget = completeButton.parentNode
    // TODO内容テキストを取得
    const text = addTarget.firstElementChild.innerText
    addTarget.textContent = null
    const p = document.createElement('p')
    p.innerText = text

    const backButton = document.createElement('button')
    backButton.innerText = '戻す'
    backButton.addEventListener('click', () => {
      const deleteTarget = backButton.parentNode
      document.getElementById('complete-list').removeChild(deleteTarget)

      const text = backButton.parentNode.firstElementChild.innerText
    })

    addTarget.appendChild(p)
    addTarget.appendChild(backButton)
    // 完了リストに追加
    document.getElementById('complete-list').appendChild(addTarget)
  })

  // 削除ボタン追加
  const deleteButton = document.createElement('button')
  deleteButton.innerText = '削除'
  deleteButton.addEventListener('click', () => {
    deleteFrom(deleteButton.parentNode)
  })

  // divの中に入れる
  div.appendChild(p)
  div.appendChild(completeButton)
  div.appendChild(deleteButton)
}

document
  .getElementById('add-button')
  .addEventListener('click', () => onClickAdd())
