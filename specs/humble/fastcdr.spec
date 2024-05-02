# Meta Package
Name:           ros-humble-fastcdr
Version:        1.0.24
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-fastcdr and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-fastcdr
Requires:       ros2-humble-fastcdr-devel

Obsoletes: ros-humble-fastcdr < 1.0.24-1

%description
CDR serialization implementation.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.24-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.24-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.24-1
- Initial humble build
