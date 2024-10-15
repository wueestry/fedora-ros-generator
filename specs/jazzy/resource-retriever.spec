# Meta Package
Name:           ros-jazzy-resource-retriever
Version:        3.4.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/resource_retriever
Summary:        Meta package for ros2-jazzy-resource_retriever and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-resource_retriever
Requires:       ros2-jazzy-resource_retriever-devel

Obsoletes: ros-jazzy-resource-retriever < 3.4.3-1

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
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.3-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.1-1
- Update to latest release
