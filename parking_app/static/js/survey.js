
            function saveToCSV() {
            // 폼 데이터 수집
            const form = document.getElementById('form');
            const formData = new FormData(form);

            // CSV 데이터 구성
            let csvContent = "data:text/csv;charset=utf-8,";
            csvContent += "Name,Vehicle Type,Price,Capacity\n"; // CSV 헤더
            csvContent += `${formData.get('name')},${formData.get('vtype')},${formData.get('price')},${formData.get('capacity')}\n`;

            // CSV 파일 생성 및 다운로드
            const encodedUri = encodeURI(csvContent);
            const link = document.createElement('a');
            link.setAttribute('href', encodedUri);
            link.setAttribute('download', 'form_data.csv');
            document.body.appendChild(link); // 다운로드 링크를 DOM에 추가
            link.click(); // 링크 클릭하여 다운로드 실행
            document.body.removeChild(link); // 다운로드 후 링크 제거
            }