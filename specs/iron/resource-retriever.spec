# Meta Package
Name:           ros-iron-resource-retriever
Version:        3.2.2
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/resource_retriever
Summary:        Meta package for ros2-iron-resource_retriever and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-resource_retriever
Requires:       ros2-iron-resource_retriever-devel

Obsoletes: ros-iron-resource-retriever < 3.2.2-1

%description
This package retrieves data from url-format files such as http://,
ftp://, package:// file://, etc., and loads the data into memory. The
package:// url for ros packages is translated into a local file://
url. The resourse retriever was initially designed to load mesh files
into memory, but it can be used for any type of data. The resource
retriever is based on the the libcurl library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.2.2-1
- Update to latest release
