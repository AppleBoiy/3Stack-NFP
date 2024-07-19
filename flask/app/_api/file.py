import os

from app.models.file import File
from flask import current_app, send_file, request
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename

file_ns = Namespace("file", description="File Upload/Download utilities")

file_model = file_ns.model(
    "File",
    {
        "id": fields.Integer(readOnly=True, description="The file identifier"),
        "filename": fields.String(required=True, description="The file name"),
        "filepath": fields.String(readOnly=True, description="The file path"),
    },
)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_ns.route("/")
class FileList(Resource):
    @file_ns.doc("list_files")
    @file_ns.marshal_list_with(file_model)
    def get(self):
        """List all files"""
        return File.query.all()


@file_ns.route("/<int:id>")
class FileDownload(Resource):
    @file_ns.doc("get_file")
    @file_ns.marshal_with(file_model)
    def get(self, id):
        """Get a file by ID"""
        file_record = File.query.get_or_404(id)
        return file_record


@file_ns.route("/upload")
class FileUpload(Resource):
    @file_ns.expect(file_ns.parser().add_argument('file', location='files', type='file', required=True))
    @file_ns.marshal_with(file_model, code=201)
    def post(self):
        """Upload a new file"""
        if 'file' not in request.files:
            return {"error": "No file part"}, 400
        file = request.files['file']
        if file.filename == '':
            return {"error": "No selected file"}, 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            new_file = File(filename=filename, filepath=filepath)
            new_file.save()
            return new_file, 201
        return {"error": "File type not allowed"}, 400


@file_ns.route("/download/<int:id>")
class FileDownloadById(Resource):
    @file_ns.doc("download_file")
    def get(self, id):
        """Download a file by ID"""
        file_record = File.query.get_or_404(id)
        filepath = file_record.filepath
        if not os.path.exists(filepath):
            return {"error": "File not found"}, 404

        # Send the file as an attachment
        return send_file(filepath, as_attachment=True)


@file_ns.route("/delete/<int:id>")
class FileDelete(Resource):
    @file_ns.doc("delete_file")
    def delete(self, id):
        """Delete a file by ID"""
        file_record = File.query.get_or_404(id)
        file_record.delete()
        print(file_record.filepath)
        return {"message": "File deleted"}, 200
