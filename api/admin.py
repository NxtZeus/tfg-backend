from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Producto, Usuario, Pedido, DetallePedido, Reembolso, Reseña

# Personalización del modelo Usuario
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'correo_electronico', 'rol', 'ciudad', 'pais']
    list_filter = ['rol', 'is_staff', 'is_active', 'ciudad', 'pais']
    search_fields = ['username', 'first_name', 'last_name', 'correo_electronico']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('direccion', 'ciudad', 'pais', 'codigo_postal', 'telefono', 'rol')}),
    )

# Registro de otros modelos
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'categoria', 'marca', 'precio', 'stock']
    list_filter = ['categoria', 'marca']
    search_fields = ['nombre_producto', 'marca']
    ordering = ['nombre_producto']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha_pedido', 'direccion_envio', 'metodo_pago', 'precio_total', 'estado_pedido']
    list_filter = ['metodo_pago', 'estado_pedido']
    search_fields = ['cliente__username', 'direccion_envio']
    ordering = ['fecha_pedido']

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio_unidad']
    list_filter = ['pedido', 'producto']
    search_fields = ['pedido__id', 'producto__nombre_producto']
    ordering = ['pedido']

class ReembolsoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'fecha_reembolso', 'precio_reembolso', 'motivo']
    list_filter = ['fecha_reembolso']
    search_fields = ['pedido__id', 'motivo']
    ordering = ['fecha_reembolso']

class ReseñaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cliente', 'calificacion', 'fecha_reseña']
    list_filter = ['producto', 'calificacion']
    search_fields = ['producto__nombre_producto', 'cliente__username', 'comentario']
    ordering = ['fecha_reseña']

# Registro de modelos en el panel de administración
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)
admin.site.register(Reembolso, ReembolsoAdmin)
admin.site.register(Reseña, ReseñaAdmin)
