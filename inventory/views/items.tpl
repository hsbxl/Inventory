<!DOCTYPE html>
<html>
<body>
    <h1>HSBXL Inventory Items</h1>
    % for item in items:
        <p>
            {{ item.get('name') }}
        </p>
    % end
</body>
</html>
