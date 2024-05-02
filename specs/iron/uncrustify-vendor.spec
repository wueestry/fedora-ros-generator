# Meta Package
Name:           ros-iron-uncrustify-vendor
Version:        2.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/uncrustify/uncrustify
Summary:        Meta package for ros2-iron-uncrustify_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-uncrustify_vendor
Requires:       ros2-iron-uncrustify_vendor-devel

Obsoletes: ros-iron-uncrustify-vendor < 2.1.2-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.2-1
- Update to latest release
