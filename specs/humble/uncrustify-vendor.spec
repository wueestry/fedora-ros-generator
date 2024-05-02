# Meta Package
Name:           ros-humble-uncrustify-vendor
Version:        2.0.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/uncrustify/uncrustify
Summary:        Meta package for ros2-humble-uncrustify_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-uncrustify_vendor
Requires:       ros2-humble-uncrustify_vendor-devel

Obsoletes: ros-humble-uncrustify-vendor < 2.0.2-1

%description
Wrapper around uncrustify, providing nothing but a dependency on
uncrustify, on some systems. On others, it provides an ExternalProject
build of uncrustify.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.2-1
- Initial humble build
