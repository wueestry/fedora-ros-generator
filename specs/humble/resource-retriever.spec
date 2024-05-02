# Meta Package
Name:           ros-humble-resource-retriever
Version:        3.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/resource_retriever
Summary:        Meta package for ros2-humble-resource_retriever and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-resource_retriever
Requires:       ros2-humble-resource_retriever-devel

Obsoletes: ros-humble-resource-retriever < 3.1.1-1

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.1-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.1-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.12.7-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.1-1
- Initial humble build
